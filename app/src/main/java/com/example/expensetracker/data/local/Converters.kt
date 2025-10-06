package com.example.expensetracker.data.local

import androidx.room.TypeConverter

class Converters {
    @TypeConverter
    fun categoryToString(category: Category): String = category.name

    @TypeConverter
    fun stringToCategory(raw: String): Category = Category.fromRaw(raw)
}
