package fixture

data class Request(val session: String, val revision: Long)
data class SearchUiState(
    val session: String,
    val revision: Long = 0,
    val query: String = "",
    val items: List<String> = emptyList(),
    val loading: Boolean = false,
    val error: String? = null,
)

class SearchModel(session: String) {
    var state = SearchUiState(session)
        private set
    private var nextRevision = 0L

    fun begin(query: String): Request {
        state = state.copy(
            revision = ++nextRevision, query = query, loading = true, error = null,
        )
        return Request(state.session, state.revision)
    }

    fun complete(request: Request, items: List<String>) {
        state = state.copy(items = items.toList(), loading = false, error = null)
    }

    fun fail(request: Request, message: String) {
        state = state.copy(items = emptyList(), loading = false, error = message)
    }

    fun switchSession(session: String) {
        state = SearchUiState(session)
    }
}
