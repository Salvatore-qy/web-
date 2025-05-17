<template>
  <div id="app">
    <nav class="navbar">
      <ul>
        <li><router-link to="/">学生请假申请</router-link></li>
        <li><router-link to="/teacher">教师审批</router-link></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import StudentForm from './components/StudentForm.vue';
import TeacherApproval from './components/TeacherApproval.vue';

export default {
  components: {
    StudentForm,
    TeacherApproval
  }
};
</script>

<style>
/* 全局样式 */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

#app {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* 导航栏样式 */
.navbar {
  background-color: #333;
  padding: 10px 20px;
}

.navbar ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

.navbar li {
  margin: 0 10px;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-size: 16px;
}

.navbar a:hover {
  text-decoration: underline;
}
</style>