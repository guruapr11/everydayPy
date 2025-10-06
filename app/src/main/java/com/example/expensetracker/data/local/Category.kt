package com.example.expensetracker.data.local

enum class Category(val displayName: String) {
    FOOD("Food"),
    TRANSPORT("Transport"),
    BILLS("Bills"),
    ENTERTAINMENT("Entertainment"),
    SHOPPING("Shopping"),
    HEALTH("Health"),
    INCOME("Income"),
    OTHER("Other");

    companion object {
        fun fromRaw(raw: String): Category = entries.firstOrNull { it.name == raw } ?: OTHER
    }
}
