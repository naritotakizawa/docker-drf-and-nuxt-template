<template>
  <div>
    <p v-if="$fetchState.pending" class="loading-wrapper">
      <span class="loading"></span>
    </p>
    <p v-else-if="$fetchState.error">何かエラーが起きています。</p>
    <div else>
      <h1>{{ response.message }}</h1>
      <button @click="$fetch">リロード</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      response: null,
    }
  },
  async fetch() {
    this.response = await this.$axios.$get('/hello/')
  },
}
</script>

<style></style>
