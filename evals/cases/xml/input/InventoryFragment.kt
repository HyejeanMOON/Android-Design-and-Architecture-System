package fixture.xml

import android.os.Bundle
import android.view.View
import androidx.fragment.app.Fragment
import fixture.xml.databinding.FragmentInventoryBinding

object RefreshHooks {
    var listener: (() -> Unit)? = null
}

class InventoryFragment : Fragment(R.layout.fragment_inventory) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val binding = FragmentInventoryBinding.bind(view)
        RefreshHooks.listener = { binding.title.text = getString(R.string.refreshed) }
    }

    override fun onDestroyView() {
        super.onDestroyView()
    }
}
