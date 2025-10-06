package com.example.expensetracker.ui.viewmodel

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.createSavedStateHandle
import androidx.lifecycle.viewmodel.initializer
import androidx.lifecycle.viewmodel.viewModelFactory
import com.example.expensetracker.ExpenseApplication
import com.example.expensetracker.ui.addedit.AddEditExpenseViewModel
import com.example.expensetracker.ui.expenses.ExpensesViewModel
import com.example.expensetracker.ui.stats.StatsViewModel

object AppViewModelProvider {
    val Factory: ViewModelProvider.Factory = viewModelFactory {
        initializer {
            val app = this[ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY] as ExpenseApplication
            ExpensesViewModel(app.container.expenseRepository)
        }
        initializer {
            val app = this[ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY] as ExpenseApplication
            AddEditExpenseViewModel(app.container.expenseRepository, createSavedStateHandle())
        }
        initializer {
            val app = this[ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY] as ExpenseApplication
            StatsViewModel(app.container.expenseRepository)
        }
    }
}
