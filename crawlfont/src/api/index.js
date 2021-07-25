import request from '../utils/request';

const baseURL = process.env.VUE_APP_BACKEND_URL;
const apiVersion = `/api/v1`;
export const apiBase = `${baseURL}${apiVersion}`;

// console.log(apiBase);


export const login = data => {
    return request({
        url: `${baseURL}/api/v1/admin/auth/login/access-token`,
        method: 'POST',
        data: data
    })
};


// 项目列表
export const projectIndex = query => {
    return request({
        url: `${apiBase}/projects`,
        method: 'GET'
    })
};

// 创建项目
export const createProject = data => {
    return request({
        url: `${apiBase}/project/create`,
        method: 'POST',
        data: data
    })
};


// 删除项目 
export const deleteProject = data => {
    return request({
        url: `${apiBase}/project/delete`,
        method: 'DELETE',
        data: data
    })
};



// 所有任务
export const taskIndex = query => {
    return request({
        url: `${apiBase}/tasks`,
        method: 'GET',
        params: query
    })
};

// 创建任务
export const createTask = data => {
    return request({
        url: `${apiBase}/task/create`,
        method: 'POST',
        data: data
    })
};

// 删除任务
export const deleteTask = data => {
    return request({
        url: `${apiBase}/task/delete`,
        method: 'DELETE',
        data: data
    })
};

// 项目下的任务列表
export const taskList = query => {
    return request({
        url: `${apiBase}/project`,
        method: 'GET',
        params: query
    })
};

// 任务详情
export const taskDetail = query => {
    return request({
        url: `${apiBase}/task/detail`,
        method: 'GET',
        params: query
    })
};

// 部署任务
export const deployTask = data => {
    return request({
        url: `${apiBase}/task/deploy`,
        method: 'POST',
        data: data
    })
};



// 开启任务
export const startTask = data => {
    return request({
        url: `${apiBase}/task/run`,
        method: 'POST',
        data: data
    })
};


// 系统参数
export const systemParams = () => {
    return request({
        url: `${apiBase}/global/system`,
        method: 'GET',
    })
};


// redis参数
export const redisParams = () => {
    return request({
        url: `${apiBase}/global/redis`,
        method: 'GET',
    })
};


// Mysql参数
export const mongoParams = () => {
    return request({
        url: `${apiBase}/global/mongodb`,
        method: 'GET',
    })
};








// 测试图表
export const systemTestCharts = () => {
    return request({
        url: `${apiBase}/system/testCharts`,
        method: 'GET',
    })
};

// 项目 任务总数量
export const projectCount = () => {
    return request({
        url: `${apiBase}/global/count`,
        method: 'GET',
    })
};

// 模拟数据
export const fetchData = query => {
    return request({
        url: `${apiBase}/spider/queryTable`,
        method: 'GET',
        params: query
    })
};

// 下载excel
export const downloadExcel = data => {
    console.log(data)
    return request({
        url: `${apiBase}/file/export`,
        method: 'POST',
        responseType: 'blob',
        data:data,
    })
};

// 上传excel
export const uploadExcel  = data => {
    return request({
        url: `${apiBase}/file/import`,
        method: 'POST',
        data:data
    })
};


// 上传excel
export const uploadWordExcel  = data => {
    return request({
        url: `${apiBase}/file/importWord`,
        method: 'POST',
        data:data
    })
};

// 上传zip包
export const uploadZip  = data => {
    return request({
        url: `${apiBase}/file/uploadZip`,
        method: 'POST',
        data:data
    })
};


// 上传文件到mongo
export const uploadWordMongo  = data => {
    return request({
        url: `${apiBase}/file/importMongo`,
        method: 'POST',
        data:data
    })
};


// mongo测试数据
export const mongoData  = query => {
    return request({
        url: `${apiBase}/utils/mongoData`,
        method: 'GET',
        params:query
    })
};

// 待办列表
export const getTodoList  = () => {
    return request({
        url: `${apiBase}/todos`,
        method: 'GET',
    })
};

// 创建待办
export const createTodo  = data => {
    return request({
        url: `${apiBase}/todo/create`,
        method: 'POST',
        data:data
    })
};

// 删除待办
export const deleteTodo  = data => {
    return request({
        url: `${apiBase}/todo/delete`,
        method: 'DELETE',
        data:data
    })
};

// 编辑待办
export const editTodo  = data => {
    return request({
        url: `${apiBase}/todo/edit`,
        method: 'PUT',
        data:data
    })
};

// 更新待办
export const updateTodo  = data => {
    return request({
        url: `${apiBase}/todo/update`,
        method: 'PUT',
        data:data
    })
};




// 工作日志列表
export const getWorkList  = () => {
    return request({
        url: `${apiBase}/workLogs`,
        method: 'GET',
    })
};

// 创建工作日志
export const createWork  = data => {
    return request({
        url: `${apiBase}/workLog/create`,
        method: 'POST',
        data:data
    })
};

// 删除工作日志
export const deleteWork  = data => {
    return request({
        url: `${apiBase}/workLog/delete`,
        method: 'DELETE',
        data:data
    })
};






// 节点列表
export const hostList = query => {
    return request({
        url: `${apiBase}/hosts`,
        method: 'GET',
        params:query
    })
};


// 节点详情
export const hostDetail  = query => {
    return request({
        url: `${apiBase}/host/detail`,
        method: 'GET',
        params:query
    })
};

// 创建节点
export const createHost  = data => {
    return request({
        url: `${apiBase}/host/create`,
        method: 'POST',
        data:data
    })
};

// 编辑节点信息
export const editHost  = data => {
    return request({
        url: `${apiBase}/host/edit`,
        method: 'PUT',
        data: data
    })
};

// 删除节点
export const deleteHost  = data => {
    return request({
        url: `${apiBase}/host/delete`,
        method: 'DELETE',
        data: data
    })
};


// 测试节点
export const testHost  = data => {
    return request({
        url: `${apiBase}/host/test`,
        method: 'POST',
        data: data
    })
};

// 节点部署服务
export const deployServer  = data => {
    return request({
        url: `${apiBase}/host/deploys`,
        method: 'PUT',
        data: data
    })
};



// rsa开关
export const changeRsaVerify  = data => {
    return request({
        url: `${apiBase}/host/changeRsaVerify`,
        method: 'POST',
        data: data
    })
};

// 获取 ssh rsa 公钥
export const getRsaPrivateKey  = data => {
    return request({
        url: `${apiBase}/host/getRsaPrivateKey`,
        method: 'POST',
        data: data
    })
};



export default {
    login,
    startTask,
    systemParams,
    downloadExcel,
    uploadExcel,
    uploadWordExcel,
    uploadWordMongo,
    mongoData,
    getTodoList,
    createTodo,
    deleteTodo,
    editTodo,
    updateTodo,
    hostList,
    createHost,
    deleteHost,
    editHost,
    testHost,
    deployServer,
    changeRsaVerify,
    getRsaPrivateKey,
    uploadZip,
    getWorkList,
    createWork,
    deleteWork,
}








