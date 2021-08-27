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
    name: "MovieDetail",
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/MovieDetail.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
