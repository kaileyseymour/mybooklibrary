<script setup>
import NavBar from './components/navBar.vue';
</script>

<template>
  <header>
    <h1>Kailey's Books</h1>
  </header>
  <nav>
    <NavBar></NavBar>
  </nav>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
h1,nav {
  padding-left: 15px;
}
</style>