let util = {

};
util.title = function (title) {
    title = title ? title + ' - Home' : 'POLE';
    window.document.title = title;
};



export default util;