var total = 0;
var pages = 0;
var limit = 0;
var htmlFirstSeparator = '<li class="page-item page-first-separator disabled"><a class="page-link" href="JavaScript:void(0);">...</a></li>';
var htmlLastSeparator = '<li class="page-item page-last-separator disabled"><a class="page-link" href="JavaScript:void(0);">...</a></li>';

function generatePageItem(pages){
    return '<li class="page-item"><a class="page-link" href="JavaScript:void(0);">'+pages+'</a></li>';
}

$(document).on("click",'.page-item',function () {
    var pageList = $(".page-item");
    var click = $(this);
    var textClick = click.text();
    var active = $(".active");
    var textActive = active.text();
    var pagePre = $(".page-pre");
    var pageNext = $(".page-next");
    var firstSeparator = $(".page-first-separator");
    var lastSeparator = $(".page-last-separator");
    // 页面只有7页及其以下的数据
    if(pages <= 7){
        if(textClick === "‹"){
            // 点击的是上一页
            if(active.text() !== "1"){
                active.removeClass("active");
                active.prev().addClass("active");
            }else{
                active.removeClass("active");
                pageNext.prev().addClass("active");
            }
        }else if(textClick === "›"){
            // 点击的是下一页
            if(active.text() !== pages+""){
                active.removeClass("active");
                active.next().addClass("active");
            }else{
                active.removeClass("active");
                pagePre.next().addClass("active");
            }
        }else{
            pageList.removeClass("active");
            $(this).addClass("active");
        }
    }else{
        // 当前点击的是第几个元素
        var indexClick = pageList.index(this);
        var indexActive = pageList.index(active);
        var textClickInt = parseInt(textClick);
        var textActiveInt = parseInt(textActive);
        if(textClick === "‹"){
            // 点击的是上一页
            if((pages-textActiveInt) === 3){
                pageNext.prev().prev().remove();
                pageNext.prev().prev().remove();
                pageNext.prev().before(htmlLastSeparator);
            }
            if(indexActive === 4){
                if(textActiveInt !== 4){
                    // 在最后一个分隔符前去掉一列
                    lastSeparator.prev().remove();
                    // 在第一个分隔符后面加入一列
                    firstSeparator.after(generatePageItem(textActiveInt-2));
                }
                if(textActiveInt === 5){
                    firstSeparator.after(generatePageItem(textActiveInt-3));
                    firstSeparator.remove();
                }
            }
            if(textActiveInt !== 1){
                active.removeClass("active");
                active.prev().addClass("active");
            }else{
                // 点击的是最后一个元素
                for(var m=0; m<5; m++){
                    pageNext.prev().prev().remove();
                }
                for(var n=0; n<4; n++){
                    pageNext.prev().before(generatePageItem(pages-4+n));
                }
                pagePre.next().after(htmlFirstSeparator);
                active.removeClass("active");
                pageNext.prev().addClass("active");
            }
        }else if(textClick === "›"){
            // 点击的是下一页
            if(textActiveInt === 4){
                // 移除2个列
                pagePre.next().next().remove();
                pagePre.next().next().remove();
                // 添加第一个分隔符
                pagePre.next().after(htmlFirstSeparator);
            }
            if(indexActive === 4){
                if((pages - textActiveInt) !== 3){
                    firstSeparator.next().remove();
                    // 在最后一个分隔符前添加一列
                    lastSeparator.before(generatePageItem(textActiveInt+2));
                }
                if((pages - textActiveInt) === 4){
                    lastSeparator.before(generatePageItem(textActiveInt+3));
                    lastSeparator.remove();
                }
            }
            if(textActiveInt !== pages){
                active.removeClass("active");
                active.next().addClass("active");
            }else{
                for(var o=0; o<5; o++){
                    pagePre.next().next().remove();
                }
                for(var p=0; p<4; p++){
                    pagePre.next().after(generatePageItem(5-p));
                }
                pageNext.prev().before(htmlLastSeparator);
                active.removeClass("active");
                pagePre.next().addClass("active");
            }
        }else{
            if(indexClick === 7){
                // 点击的是最后一个元素
                for(var i=0; i<5; i++){
                    pageNext.prev().prev().remove();
                }
                for(var j=0; j<4; j++){
                    pageNext.prev().before(generatePageItem(pages-4+j));
                }
                pagePre.next().after(htmlFirstSeparator);
            }else if(indexClick === 5){
                if(textClickInt === 5){
                    // 移除2个列
                    pagePre.next().next().remove();
                    pagePre.next().next().remove();
                    // 添加第一个分隔符
                    pagePre.next().after(htmlFirstSeparator);
                    // 当前页码后再添加一个页码
                    $(this).after(generatePageItem(6));
                    // 判断是否去掉最后一个分隔符
                    if((pages - textClickInt) === 3){
                        lastSeparator.before(generatePageItem(pages-1));
                        lastSeparator.remove();
                    }
                }else{
                    if((pages - textClickInt) !== 2){
                        // 移除前一个分隔符后面的一列
                        firstSeparator.next().remove();
                        // 在后一个分隔符前面加入一列
                        lastSeparator.before(generatePageItem(textClickInt+1));
                        // 判断是否去掉最后一个分隔符
                        if((pages - textClickInt) === 3){
                            lastSeparator.before(generatePageItem(pages-1));
                            lastSeparator.remove();
                        }
                    }
                }
            }else if(indexClick === 4){
                // 无变化
            }else if(indexClick === 3){
                if((pages - textClickInt) === 4){
                    pageNext.prev().prev().remove();
                    pageNext.prev().prev().remove();
                    pageNext.prev().before(htmlLastSeparator);
                }
                if(textClickInt !== 3){
                    // 移除后一个分隔符前面的一列
                    lastSeparator.prev().remove();
                    // 在第一个分隔符前面加入一列
                    firstSeparator.after(generatePageItem(textClickInt-1));
                    // 如果点击的数字是4，再在第一个分隔符前面加入一列，同时移除第一个分隔符
                    if(textClickInt === 4){
                        firstSeparator.after(generatePageItem(2));
                        firstSeparator.remove();
                    }
                }
            }else if(indexClick === 1){
                // 点击的是第一个元素
                for(var k=0; k<5; k++){
                    pagePre.next().next().remove();
                }
                for(var l=0; l<4; l++){
                    pagePre.next().after(generatePageItem(5-l));
                }
                pageNext.prev().before(htmlLastSeparator);
            }
            if(textClick !== "..."){
                pageList.removeClass("active");
                $(this).addClass("active");
            }
        }
    }
    updatePaginationDetail(parseInt($(".active").text()));
});

function initSpiritPagination(total, pages, limit){
    this.total = total;
    this.pages = pages;
    this.limit = limit;
    var html = '';
    var commonHead = '<div class="float-left pagination-detail">' +
        '<span class="pagination-info">' +
        '显示第 1 到第 '+limit+' 条记录，总共 '+total+' 条记录' +
        '</span>' +
        '</div>' +
        '<div class="float-right pagination">' +
        '<ul class="pagination">' +
        '<li class="page-item page-pre"><a class="page-link" href="JavaScript:void(0);">‹</a></li>'+
        '<li class="page-item active"><a class="page-link" href="JavaScript:void(0);">1</a></li>';
    if(pages === 0){
        html =  '<div class="float-left pagination-detail">' +
            '<span class="pagination-info">' +
            '显示第 0 到第 0 条记录，总共 0 条记录' +
            '</span>' +
            '</div>';
    }else if(pages === 1){//只有一页数据
        html =  '<div class="float-left pagination-detail">' +
            '<span class="pagination-info">' +
            '显示第 1 到第 '+total+' 条记录，总共 '+total+' 条记录' +
            '</span>' +
            '</div>';
    }else if(pages <= 7){
        html =  commonHead;
        for(var i=1; i< pages; i++){
            html += '<li class="page-item"><a class="page-link" href="JavaScript:void(0);">'+(i+1)+'</a></li>';
        }
        html += '<li class="page-item page-next"><a class="page-link" href="JavaScript:void(0);">›</a></li>'+
            '</ul></div>';
    }else if(pages > 7){
        html =  commonHead;
        for(var j=0; j< 4; j++){
            html += '<li class="page-item"><a class="page-link" href="JavaScript:void(0);">'+(j+2)+'</a></li>';
        }
        html += '<li class="page-item page-last-separator disabled"><a class="page-link" href="JavaScript:void(0);">...</a></li>'+
            '<li class="page-item"><a class="page-link" href="JavaScript:void(0);">'+pages+'</a></li>'+
            '<li class="page-item page-next"><a class="page-link" href="JavaScript:void(0);">›</a></li>'+
            '</ul></div>';
    }
    $(".spiritPagination").html(html);
}

function updatePaginationDetail(pages){
    var from = (pages-1) * this.limit + 1;
    var to = pages * this.limit;
    if(pages === this.pages){
        to = this.total;
    }
    var html = '显示第 '+from+' 到第 '+to+' 条记录，总共 '+this.total+' 条记录';
    $(".pagination-info").html(html);
    updateViewInfo(pages, this.limit);
}