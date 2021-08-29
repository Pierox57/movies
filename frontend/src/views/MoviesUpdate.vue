<template>
  <div class="movies-update">
    <h2>Update</h2>
    <div class="container m-auto w-1/2">
      <form @submit="checkForm" class="flex flex-col">
        <div v-if="form_errors.length" class="mb-2">
          <p class="font-bold">Please correct the following error(s):</p>
          <ul>
            <li v-for="error in form_errors" :key="error" class="text-red-500">
              {{ error }}
            </li>
          </ul>
        </div>
        <input
          type="text"
          name="title"
          placeholder="Title"
          v-model="movie.title"
        />
        <textarea
          name="description"
          placeholder="Description"
          cols="30"
          rows="10"
          v-model="movie.description"
        >
        </textarea>
        <select multiple v-model="movie.actors">
          <option v-for="actor in actors" :key="actor" :value="actor">
            {{ actor.first_name }} {{ actor.last_name }}
          </option>
        </select>
        <button @click="setMovie" class="my-2">Update</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "MoviesUpdate",
  data() {
    return {
      form_errors: [],
    };
  },
  computed: {
    ...mapState(["movie", "actors", "error"]),
  },
  methods: {
    ...mapActions(["getMovie", "getActors", "updateMovie"]),
    setMovie() {
      if (!this.form_errors.length) {
        this.updateMovie(this.movie)
          .then(() => {
            this.$router.push({
              name: "MoviesDetail",
              params: { id: this.movie.id },
            });
          })
          .catch(() => {
            console.error(this.error);
          });
      }
    },
    checkForm(element) {
      if (this.title && this.description) {
        return true;
      }

      this.form_errors = [];

      if (!this.title) {
        this.form_errors.push("Title field is mandatory.");
      }
      if (!this.description) {
        this.form_errors.push("Description field is mandatory.");
      }

      element.preventDefault();
    },
  },
  mounted() {
    this.getMovie(this.$route.params.id).catch(() => {
      console.error(this.error);
    });
    this.getActors().catch(() => {
      console.error(this.error);
    });
  },
};
</script>
