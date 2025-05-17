import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Student from '../views/Student.vue';
import Teacher from '../views/Teacher.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/student',
    name: 'Student',
    component: Student
  },
  {
    path: '/teacher',
    name: 'Teacher',
    component: Teacher
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;