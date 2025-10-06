package com.example.expensetracker.di

import android.content.Context
import com.example.expensetracker.data.DefaultExpenseRepository
import com.example.expensetracker.data.ExpenseRepository
import com.example.expensetracker.data.local.AppDatabase

class AppContainer(context: Context) {
    private val database: AppDatabase = AppDatabase.getInstance(context)
    val expenseRepository: ExpenseRepository = DefaultExpenseRepository(database.expenseDao())
}
