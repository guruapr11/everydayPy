package com.example.expensetracker.ui.navigation

sealed class NavRoute(val route: String) {
    data object Expenses : NavRoute("expenses")
    data object AddEditExpense : NavRoute("add_edit?expenseId={expenseId}") {
        fun createRoute(expenseId: Long?): String =
            if (expenseId == null) "add_edit?expenseId=-1" else "add_edit?expenseId=$expenseId"
    }
}
