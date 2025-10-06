package com.example.expensetracker

import android.app.Application
import com.example.expensetracker.di.AppContainer

class ExpenseApplication : Application() {
    lateinit var container: AppContainer
        private set

    override fun onCreate() {
        super.onCreate()
        container = AppContainer(this)
    }
}
