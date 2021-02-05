<template>
  <div>
    <h2 v-for="user in users" :key="user.id">{{ user.username }}</h2>
    <button @click="$fetch">リロード</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      users: [],
    }
  },
  async fetch() {
    this.users = await this.$axios.$get('/auth/users/')
  },
}
</script>

<style></style>
