package com.example.expensetracker.data.local

import androidx.room.Dao
import androidx.room.Delete
import androidx.room.Query
import androidx.room.Upsert
import kotlinx.coroutines.flow.Flow

@Dao
interface ExpenseDao {
    @Query("SELECT * FROM expenses ORDER BY timestampMillis DESC")
    fun observeAll(): Flow<List<Expense>>

    @Query("SELECT * FROM expenses WHERE id = :id")
    fun observeById(id: Long): Flow<Expense?>

    @Upsert
    suspend fun upsert(expense: Expense): Long

    @Delete
    suspend fun delete(expense: Expense)

    @Query("DELETE FROM expenses WHERE id = :id")
    suspend fun deleteById(id: Long)

    @Query("SELECT SUM(amountInCents) FROM expenses")
    fun observeTotalInCents(): Flow<Long?>

    @Query("SELECT SUM(amountInCents) FROM expenses WHERE timestampMillis BETWEEN :fromMillis AND :toMillis")
    fun observeTotalInCentsBetween(fromMillis: Long, toMillis: Long): Flow<Long?>
}
