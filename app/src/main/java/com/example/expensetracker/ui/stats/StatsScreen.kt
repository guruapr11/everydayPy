package com.example.expensetracker.ui.stats

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.expensetracker.ui.components.AmountText

@Composable
fun StatsScreen(state: StatsState) {
    Scaffold(topBar = { TopAppBar(title = { Text("Stats") }) }) { padding ->
        Column(Modifier.fillMaxSize().padding(padding).padding(16.dp)) {
            Text("Total Spent")
            AmountText(state.monthlyTotalInCents)
        }
    }
}
