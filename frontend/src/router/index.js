import { createRouter, createWebHistory } from "vue-router";
import MoviesList from "../views/MoviesList.vue";

const routes = [
  {
    path: "/",
    name: "MoviesList",
    component: MoviesList,
  },
  {
    path: "/detail/:id",
    name: "MoviesDetail",
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/MoviesDetail.vue"),
  },
  {
    path: "/Update/:id",
    name: "MoviesUpdate",
    component: () =>
      import(/* webpackChunkName: "update" */ "../views/MoviesUpdate.vue"),
  },
  {
    path: "/reviews/add/:id",
    name: "ReviewsAdd",
    component: () =>
      import(/* webpackChunkName: "add" */ "../views/ReviewsAdd.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
