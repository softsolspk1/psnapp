package com.pakneurology.network

import android.os.Bundle
import android.view.MenuItem
import androidx.appcompat.app.ActionBarDrawerToggle
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import androidx.fragment.app.Fragment
import com.google.android.material.navigation.NavigationView
import com.pakneurology.network.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity(), NavigationView.OnNavigationItemSelectedListener {

    private lateinit var binding: ActivityMainBinding
    private lateinit var toggle: ActionBarDrawerToggle

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.toolbar)

        toggle = ActionBarDrawerToggle(
            this,
            binding.drawerLayout,
            binding.toolbar,
            R.string.navigation_drawer_open,
            R.string.navigation_drawer_close
        )
        binding.drawerLayout.addDrawerListener(toggle)
        toggle.syncState()

        binding.navView.setNavigationItemSelectedListener(this)
        binding.bottomNavigation.setOnItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_home -> loadFragment(DashboardFragment())
                R.id.nav_members -> loadFragment(MembersFragment())
                R.id.nav_chat -> loadFragment(ChatFragment())
                R.id.nav_profile -> loadFragment(ProfileFragment())
            }
            true
        }

        // Load dashboard by default
        if (savedInstanceState == null) {
            loadFragment(DashboardFragment())
        }
    }

    private fun loadFragment(fragment: Fragment) {
        supportFragmentManager.beginTransaction()
            .replace(R.id.content_frame, fragment)
            .commit()
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.nav_home -> loadFragment(DashboardFragment())
            R.id.nav_about -> loadFragment(AboutFragment())
            R.id.nav_news -> loadFragment(NewsFragment())
            R.id.nav_events -> loadFragment(EventsFragment())
            R.id.nav_projects -> loadFragment(ProjectsFragment())
            R.id.nav_forum -> loadFragment(ForumFragment())
            R.id.nav_articles -> loadFragment(ArticlesFragment())
            R.id.nav_resources -> loadFragment(ResourcesFragment())
            R.id.nav_chat -> loadFragment(ChatFragment())
            R.id.nav_members -> loadFragment(MembersFragment())
            R.id.nav_logout -> {
                // Handle logout
                finish()
            }
        }
        binding.drawerLayout.closeDrawer(GravityCompat.START)
        return true
    }

    override fun onBackPressed() {
        if (binding.drawerLayout.isDrawerOpen(GravityCompat.START)) {
            binding.drawerLayout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }
} 