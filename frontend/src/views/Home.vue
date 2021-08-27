<template>
  <div class="home">
    <Movie msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import Movie from "@/components/Movie.vue";

export default {
  name: "Home",
  components: {
    Movie,
  },
};
</script>
