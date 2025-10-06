package com.example.expensetracker.ui.expenses

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.expensetracker.data.ExpenseRepository
import com.example.expensetracker.data.local.Expense
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

data class ExpensesUiState(
    val expenses: List<Expense> = emptyList(),
    val totalInCents: Long = 0L
)

class ExpensesViewModel(
    private val repository: ExpenseRepository
) : ViewModel() {

    val state: StateFlow<ExpensesUiState> = combine(
        repository.observeExpenses(),
        repository.observeTotalInCents()
    ) { list, total ->
        ExpensesUiState(expenses = list, totalInCents = total)
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = ExpensesUiState()
    )

    fun deleteById(id: Long) {
        viewModelScope.launch {
            repository.deleteById(id)
        }
    }
}
