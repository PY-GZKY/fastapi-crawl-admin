<template>
  <div>
    <el-card style="border-radius: 0">

      
    <el-select v-model="value" placeholder="请选择仓库">
      <el-option
        v-for="item in options1"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        v-model="item.value"
        :disabled="item.disabled"
      >
      </el-option>
    </el-select>

    <el-select v-model="value" placeholder="请选择品牌">
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        v-model="item.value"
        :disabled="item.disabled"
      >
      </el-option>
    </el-select>

    <el-select v-model="value" placeholder="请选择品类">
      <el-option
        v-for="item in options2"
        :key="item.value"
        :label="item.label"
        :value="item.value"
        :disabled="item.disabled"
        v-model="item.value"
      >
      </el-option>
    </el-select>

    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "en",
      options1: [
        {
          value: "选项1",
          label: "本仓",
        },
        {
          value: "选项2",
          label: "京东赞晓仓",
          disabled: true,
        },
        {
          value: "选项3",
          label: "京东佳皓仓",
        },
        {
          value: "选项4",
          label: "菜鸟仓",
        },
      ],
      options: [
        {
          value: "选项1",
          label: "惠普",
        },
        {
          value: "选项2",
          label: "微星",
        },

      ],

       options2: [
        {
          value: "选项1",
          label: "笔记本电脑A",
        },
        {
          value: "选项2",
          label: "笔记本电脑B",
        },

      ],


    };
  },
  created() {
    console.log(this.options);
     console.log(this.options1);
      console.log(this.options2);
  },


};
</script>

