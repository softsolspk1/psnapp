package com.pakneurology.network

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.pakneurology.network.databinding.FragmentDashboardBinding

class DashboardFragment : Fragment() {

    private var _binding: FragmentDashboardBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentDashboardBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Set click listeners for all cards
        binding.cardNews.setOnClickListener { showFeatureMessage("News") }
        binding.cardEvents.setOnClickListener { showFeatureMessage("Events") }
        binding.cardProjects.setOnClickListener { showFeatureMessage("Projects") }
        binding.cardForum.setOnClickListener { showFeatureMessage("Forum") }
        binding.cardArticles.setOnClickListener { showFeatureMessage("Articles") }
        binding.cardResources.setOnClickListener { showFeatureMessage("Resources") }
        binding.cardChat.setOnClickListener { showFeatureMessage("Chat") }
        binding.cardMembers.setOnClickListener { showFeatureMessage("Members") }
    }

    private fun showFeatureMessage(feature: String) {
        Toast.makeText(context, "$feature feature will be implemented in the final version", Toast.LENGTH_SHORT).show()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
} 