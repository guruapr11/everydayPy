package com.example.expensetracker.ui.navigation

import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.example.expensetracker.ui.addedit.AddEditExpenseScreen
import com.example.expensetracker.ui.addedit.AddEditExpenseViewModel
import com.example.expensetracker.ui.expenses.ExpensesScreen
import com.example.expensetracker.ui.expenses.ExpensesViewModel
import com.example.expensetracker.ui.stats.StatsScreen
import com.example.expensetracker.ui.stats.StatsViewModel
import com.example.expensetracker.ui.viewmodel.AppViewModelProvider

@Composable
fun ExpenseNavHost() {
    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = NavRoute.Expenses.route
    ) {
        composable(NavRoute.Expenses.route) {
            val vm: ExpensesViewModel = viewModel(factory = AppViewModelProvider.Factory)
            ExpensesScreen(
                state = vm.state,
                onAddClicked = { navController.navigate(NavRoute.AddEditExpense.createRoute(null)) },
                onEditClicked = { id -> navController.navigate(NavRoute.AddEditExpense.createRoute(id)) },
                onDelete = vm::deleteById
            )
        }
        composable(
            route = "add_edit?expenseId={expenseId}",
            arguments = listOf(
                navArgument("expenseId") { type = NavType.LongType; defaultValue = -1L }
            )
        ) {
            val vm: AddEditExpenseViewModel = viewModel(factory = AppViewModelProvider.Factory)
            AddEditExpenseScreen(
                state = vm.state,
                onTitleChange = vm::updateTitle,
                onAmountChange = vm::updateAmount,
                onSave = {
                    vm.save()
                    navController.popBackStack()
                },
                onCancel = { navController.popBackStack() }
            )
        }
        composable("stats") {
            val vm: StatsViewModel = viewModel(factory = AppViewModelProvider.Factory)
            StatsScreen(state = vm.state)
        }
    }
}
