package com.example.expensetracker.ui.components

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable

@Composable
fun AmountText(amountInCents: Long) {
    val formatted = String.format("$%.2f", amountInCents / 100.0)
    Text(text = formatted, style = MaterialTheme.typography.titleMedium)
}
