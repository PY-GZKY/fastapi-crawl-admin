<!--

<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i>爬虫
                </el-breadcrumb-item>
                <el-breadcrumb-item>爬虫详情</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="form-box">
                <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="爬虫名称" style="font-weight: bold; font-size: 20px">
                    <el-col>{{detail.title}}</el-col>
                    </el-form-item>
                    <el-form-item label="选择器" style="font-weight: bold; font-size: 20px">
                        <el-select v-model="form.region" placeholder="请选择">
                            <el-option key="xpath" label="xpath" value="xpath"></el-option>
                            <el-option key="css" label="css" value="xtc"></el-option>
                            <el-option key="json" label="json" value="json"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="日期时间" style="font-weight: bold; font-size: 20px">
                        <el-col :span="11">
                            <el-date-picker
                                    type="date"
                                    placeholder="选择日期"
                                    v-model="form.date"
                                    value-format="yyyy-MM-dd"
                                    style="width: 100%;"
                            ></el-date-picker>
                        </el-col>
                        <el-col class="line" :span="2">-</el-col>
                        <el-col :span="11">
                            <el-time-picker
                                    placeholder="选择时间"
                                    v-model="form.date_time"
                                    style="width: 100%;"
                            ></el-time-picker>
                        </el-col>
                    </el-form-item>

                    <el-form-item label="选择开关" style="font-weight: bold; font-size: 20px">
                        <el-switch v-model="form.delivery"></el-switch>
                    </el-form-item>

                    <el-form-item label="文本框" style="font-weight: bold; font-size: 20px">
                        <el-input style="font-weight: bold; font-size: 15px" type="textarea" rows="5" v-model="form.cookie"></el-input>
                    </el-form-item>

                    <el-form-item label="并发度" style="font-weight: bold; font-size: 20px">

                        <el-slider v-model="form.bing"></el-slider>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="onSubmit">表单提交</el-button>
                        <el-button>取消</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>


<style>

</style>

<script>
    import {spiderDetail, startSpider} from '../../api/index';

    export default {
        name: 'baseform',
        data() {
            return {
                form: {
                    region: '',
                    date: '',
                    date_time: '',
                    delivery: true,
                    cookie: 'Cookie ....',
                    bing: 60,
                },
                detail: {},
            };
        },
        created() {
            this.loadDetail();
        },
        methods: {

            loadDetail() {
                spiderDetail().then(res => {
                    console.log(res);
                    this.detail = res;
                });
            },
            onSubmit() {
                console.log(this.form);
                var data = {
                    'd_cookie':this.form.cookie,
                    'date':this.form.date,
                    'date_time':this.form.date_time,
                    'region':this.form.region,
                };
                console.log(data);
                startSpider(data).then(res => {
                    console.log(res);

                });
                this.$message.success("行了");
            }
        }
    };
</script>

-->
