package com.example.expensetracker.data

import com.example.expensetracker.data.local.Expense
import kotlinx.coroutines.flow.Flow

interface ExpenseRepository {
    fun observeExpenses(): Flow<List<Expense>>
    fun observeExpense(id: Long): Flow<Expense?>
    fun observeTotalInCents(): Flow<Long>
    suspend fun upsert(expense: Expense): Long
    suspend fun delete(expense: Expense)
    suspend fun deleteById(id: Long)
}
