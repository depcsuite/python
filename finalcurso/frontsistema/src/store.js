import { createStore } from "vuex";
export default createStore( {
    state: {
        isLog: localStorage.getItem('isLog') || false,
        token: '',
        uid: 0
    },
    mutations: {
        logUser(state, token, uid) {
            state.token = token;
            state.uid = uid;
            state.isLog = true;
        },
        unLogUser(state) {
            state.token = '';
            state.uid = 0;
            state.isLog = false;
        }


    },
    action: {},
    getters: {
        getToken: state => {return state.token},
        getIsLog: state => {return state.isLog}
    }




});