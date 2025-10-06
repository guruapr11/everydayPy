package com.example.expensetracker.ui.stats

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.expensetracker.data.ExpenseRepository
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn


data class StatsState(
    val monthlyTotalInCents: Long = 0L
)

class StatsViewModel(
    private val repository: ExpenseRepository
) : ViewModel() {

    val state: StateFlow<StatsState> = repository.observeTotalInCents()
        .map { total -> StatsState(monthlyTotalInCents = total) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), StatsState())
}
