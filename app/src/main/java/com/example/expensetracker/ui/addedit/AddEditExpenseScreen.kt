package com.example.expensetracker.ui.addedit

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.expensetracker.data.local.Category
import com.example.expensetracker.data.local.Expense

@Composable
fun AddEditExpenseScreen(
    state: AddEditUiState,
    onTitleChange: (String) -> Unit,
    onAmountChange: (String) -> Unit,
    onSave: () -> Unit,
    onCancel: () -> Unit
) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Add Expense") }) }
    ) { padding ->
        Content(
            padding,
            state = state,
            onTitleChange = onTitleChange,
            onAmountChange = onAmountChange,
            onSave = onSave,
            onCancel = onCancel
        )
    }
}

@Composable
private fun Content(
    padding: PaddingValues,
    state: AddEditUiState,
    onTitleChange: (String) -> Unit,
    onAmountChange: (String) -> Unit,
    onSave: () -> Unit,
    onCancel: () -> Unit
) {
    Column(Modifier.fillMaxSize().padding(padding).padding(16.dp)) {
        OutlinedTextField(value = state.title, onValueChange = onTitleChange, label = { Text("Title") })
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(value = state.amount, onValueChange = onAmountChange, label = { Text("Amount") })
        Spacer(Modifier.height(8.dp))
        Text("Category: ${Category.OTHER.displayName}")
        Spacer(Modifier.height(16.dp))
        Button(onClick = onSave) { Text("Save") }
    }
}
