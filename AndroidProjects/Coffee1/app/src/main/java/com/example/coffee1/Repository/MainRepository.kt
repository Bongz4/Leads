package com.example.coffee1.Repository

class MainRepository {
    private val firebaseDatabase = FirebaseDatabase.getInstance()

    fun loadBanner(): LiveData<NutableLiveData<MutableList<BannerMode>>()>
}