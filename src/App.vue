<template>
  <div id="app">
    <StudentForm />
  </div>
</template>

<script>
// 引入 StudentForm 组件
import students from './components/students.vue';

export default {
  components: {
    StudentForm
  }
};
</script>

<style>
/* 可以在这里添加全局样式 */
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
</style>