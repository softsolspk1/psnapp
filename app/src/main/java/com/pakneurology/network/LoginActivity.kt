package com.pakneurology.network

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.pakneurology.network.databinding.ActivityLoginBinding

class LoginActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLoginBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLoginBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.loginButton.setOnClickListener {
            val email = binding.emailInput.text.toString()
            val password = binding.passwordInput.text.toString()

            // Demo credentials
            if (email == "demo@psn.com" && password == "demo123") {
                startActivity(Intent(this, MainActivity::class.java))
                finish()
            } else {
                Toast.makeText(this, "Please use demo credentials:\nEmail: demo@psn.com\nPassword: demo123", Toast.LENGTH_LONG).show()
            }
        }

        binding.forgotPassword.setOnClickListener {
            Toast.makeText(this, "Forgot password functionality will be implemented in the final version", Toast.LENGTH_SHORT).show()
        }
    }
} 