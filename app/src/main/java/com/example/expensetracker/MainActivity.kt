package com.example.expensetracker

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import com.example.expensetracker.ui.navigation.ExpenseNavHost
import com.example.expensetracker.ui.theme.ExpenseTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ExpenseTheme {
                Surface(color = MaterialTheme.colorScheme.background) {
                    ExpenseNavHost()
                }
            }
        }
    }
}
