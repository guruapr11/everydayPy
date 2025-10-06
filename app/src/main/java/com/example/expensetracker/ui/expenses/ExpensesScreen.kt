package com.example.expensetracker.ui.expenses

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Edit
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.expensetracker.data.local.Expense
import com.example.expensetracker.ui.components.AmountText

@Composable
fun ExpensesScreen(
    state: ExpensesUiState,
    onAddClicked: () -> Unit,
    onEditClicked: (Long) -> Unit,
    onDelete: (Long) -> Unit
) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Expenses") }) },
        floatingActionButton = {
            FloatingActionButton(onClick = onAddClicked) {
                Icon(Icons.Default.Add, contentDescription = "Add")
            }
        }
    ) { padding ->
        Column(Modifier.fillMaxSize().padding(padding)) {
            if (state.expenses.isEmpty()) {
                Column(
                    Modifier.fillMaxSize().padding(24.dp),
                    verticalArrangement = Arrangement.Center
                ) {
                    Text("No expenses yet. Tap + to add.")
                }
            } else {
                LazyColumn(Modifier.fillMaxSize()) {
                    items(state.expenses) { expense ->
                        ExpenseRow(expense = expense, onEditClicked = onEditClicked, onDelete = onDelete)
                    }
                }
            }
        }
    }
}

@Composable
private fun ExpenseRow(
    expense: Expense,
    onEditClicked: (Long) -> Unit,
    onDelete: (Long) -> Unit
) {
    Row(Modifier.fillMaxWidth().padding(16.dp)) {
        Column(Modifier.weight(1f)) {
            Text(expense.title, style = MaterialTheme.typography.titleMedium)
            Spacer(Modifier.height(4.dp))
            Text(expense.category.displayName, style = MaterialTheme.typography.bodyMedium)
        }
        Column(horizontalAlignment = androidx.compose.ui.Alignment.End) {
            AmountText(expense.amountInCents)
            Row {
                IconButton(onClick = { onEditClicked(expense.id) }) {
                    Icon(Icons.Default.Edit, contentDescription = "Edit")
                }
                IconButton(onClick = { onDelete(expense.id) }) {
                    Icon(Icons.Default.Delete, contentDescription = "Delete")
                }
            }
        }
    }
}
