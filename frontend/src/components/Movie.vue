<template>
  <router-link :to="{ name: 'MoviesDetail', params: { id: id } }">
    <li class="flex-initial bg-gray-100 hover:bg-gray-200 rounded mb-2 p-2">
      <p class="font-rubik text-lg">{{ title }}</p>
    </li>
  </router-link>
</template>

<script>
export default {
  name: "Movie",
  props: {
    id: Number,
    title: String,
  },
};
</script>
