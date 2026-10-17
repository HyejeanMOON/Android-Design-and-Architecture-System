package fixture

fun main() {
    var failures = 0
    fun scenario(name: String, body: () -> Unit) {
        try {
            body()
            println("PASS $name")
        } catch (failure: IllegalStateException) {
            failures++
            println("FAIL $name: ${failure.message}")
        }
    }

    scenario("latest-response-wins") {
        val model = SearchModel("A")
        val older = model.begin("old")
        val newer = model.begin("new")
        model.complete(newer, listOf("new-result"))
        model.complete(older, listOf("old-result"))
        check(model.state.items == listOf("new-result")) { "old response replaced new data" }
    }
    scenario("old-failure-does-not-stop-current-request") {
        val model = SearchModel("A")
        val older = model.begin("old")
        model.begin("new")
        model.fail(older, "stale-error")
        check(model.state.loading && model.state.error == null) { "old failure changed current state" }
    }
    scenario("session-switch-isolates-response") {
        val model = SearchModel("A")
        val oldSession = model.begin("private")
        model.switchSession("B")
        model.complete(oldSession, listOf("A-private-result"))
        check(model.state.session == "B" && model.state.items.isEmpty()) { "cross-account data visible" }
    }
    scenario("same-query-has-distinct-request-identity") {
        val model = SearchModel("A")
        val first = model.begin("same")
        val second = model.begin("same")
        model.complete(second, listOf("second-result"))
        model.complete(first, listOf("first-result"))
        check(model.state.items == listOf("second-result")) { "query text used as request identity" }
    }
    scenario("refresh-failure-keeps-content") {
        val model = SearchModel("A")
        model.complete(model.begin("query"), listOf("cached"))
        model.fail(model.begin("query"), "offline")
        check(model.state.items == listOf("cached") && model.state.error == "offline") {
            "refresh failure lost existing content"
        }
    }
    scenario("ordinary-success-and-error-recovery") {
        val model = SearchModel("A")
        model.fail(model.begin("query"), "offline")
        model.complete(model.begin("query"), listOf("restored"))
        check(!model.state.loading && model.state.error == null && model.state.items == listOf("restored")) {
            "normal success failed"
        }
    }
    check(failures == 0) { "$failures behavioral scenario(s) failed" }
}
