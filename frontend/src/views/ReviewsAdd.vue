<template>
  <div class="reviews-create">
    <h2>Create a review for : {{ movie.title }}</h2>
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
          type="number"
          min="1"
          max="5"
          required
          name="grade"
          placeholder="Grade"
          v-model="grade"
        />
        <button @click="setReview" class="my-2">Create</button>
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
      grade: Number,
      form_errors: [],
    };
  },
  computed: {
    ...mapState(["movie", "error"]),
  },
  methods: {
    ...mapActions(["getMovie", "createReview"]),
    setReview() {
      const review = {
        grade: this.grade,
        movie: this.movie.id,
      };
      this.createReview(review)
        .then(() => {
          this.$router.push({
            name: "MoviesDetail",
            params: { id: this.movie.id },
          });
        })
        .catch(() => {
          console.error(this.error);
        });
    },
    checkForm(element) {
      if (this.grade >= 5 && this.grade <= 1) {
        return true;
      }

      this.form_errors = [];

      if (!this.grade >= 5 && !this.grade <= 1) {
        this.form_errors.push("Grade must be between 1 and 5");
      }

      element.preventDefault();
    },
  },
  mounted() {
    this.getMovie(this.$route.params.id).catch(() => {
      console.error(this.error);
    });
  },
};
</script>
