package com.example.expensetracker.ui.addedit

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.expensetracker.data.ExpenseRepository
import com.example.expensetracker.data.local.Category
import com.example.expensetracker.data.local.Expense
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

data class AddEditUiState(
    val id: Long? = null,
    val title: String = "",
    val amount: String = "",
    val category: Category = Category.OTHER,
    val note: String = ""
)

class AddEditExpenseViewModel(
    private val repository: ExpenseRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val _state = MutableStateFlow(AddEditUiState())
    val state: StateFlow<AddEditUiState> = _state.asStateFlow()

    init {
        val idArg: Long? = savedStateHandle.get<Long>("expenseId")?.takeIf { it > 0 }
        if (idArg != null) {
            viewModelScope.launch {
                repository.observeExpense(idArg).collect { expense ->
                    if (expense != null) {
                        _state.update {
                            it.copy(
                                id = expense.id,
                                title = expense.title,
                                amount = (expense.amountInCents / 100.0).toString(),
                                category = expense.category,
                                note = expense.note.orEmpty()
                            )
                        }
                    }
                }
            }
        }
    }

    fun updateTitle(newTitle: String) = _state.update { it.copy(title = newTitle) }
    fun updateAmount(newAmount: String) = _state.update { it.copy(amount = newAmount) }
    fun updateCategory(newCategory: Category) = _state.update { it.copy(category = newCategory) }
    fun updateNote(newNote: String) = _state.update { it.copy(note = newNote) }

    fun save() {
        viewModelScope.launch {
            val current = _state.value
            val cents = ((current.amount.toDoubleOrNull() ?: 0.0) * 100).toLong()
            val expense = Expense(
                id = current.id ?: 0L,
                title = current.title.trim(),
                amountInCents = cents,
                category = current.category,
                note = current.note.ifBlank { null }
            )
            repository.upsert(expense)
        }
    }
}
