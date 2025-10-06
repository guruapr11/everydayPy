package com.example.expensetracker.data.local

import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey

@Entity(
    tableName = "expenses",
    indices = [Index(value = ["timestampMillis"]) , Index(value = ["category"])]
)
data class Expense(
    @PrimaryKey(autoGenerate = true) val id: Long = 0L,
    val title: String,
    val amountInCents: Long,
    val category: Category,
    val timestampMillis: Long = System.currentTimeMillis(),
    val note: String? = null
)
