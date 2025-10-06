package com.example.expensetracker.data

import com.example.expensetracker.data.local.Expense
import com.example.expensetracker.data.local.ExpenseDao
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class DefaultExpenseRepository(
    private val expenseDao: ExpenseDao
) : ExpenseRepository {
    override fun observeExpenses(): Flow<List<Expense>> = expenseDao.observeAll()

    override fun observeExpense(id: Long): Flow<Expense?> = expenseDao.observeById(id)

    override fun observeTotalInCents(): Flow<Long> = expenseDao.observeTotalInCents().map { it ?: 0L }

    override suspend fun upsert(expense: Expense): Long = expenseDao.upsert(expense)

    override suspend fun delete(expense: Expense) = expenseDao.delete(expense)

    override suspend fun deleteById(id: Long) = expenseDao.deleteById(id)
}
