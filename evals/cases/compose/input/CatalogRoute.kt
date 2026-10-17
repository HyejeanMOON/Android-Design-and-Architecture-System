package fixture.compose

import androidx.compose.foundation.text.BasicText
import androidx.compose.runtime.Composable
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

data class CatalogUiState(val label: String = "Catalog")

class CatalogViewModel(private val refresh: () -> Unit) : ViewModel() {
    private val state = MutableStateFlow(CatalogUiState())
    val uiState = state.asStateFlow()
    fun refreshCatalog() = refresh()
    fun updateLabel(label: String) { state.value = CatalogUiState(label) }
}

@Composable
fun CatalogRoute(viewModel: CatalogViewModel) {
    val state = viewModel.uiState.collectAsStateWithLifecycle().value
    viewModel.refreshCatalog()
    CatalogScreen(state)
}

@Composable
fun CatalogScreen(state: CatalogUiState) {
    BasicText(state.label)
}
