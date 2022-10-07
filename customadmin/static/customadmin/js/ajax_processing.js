/*global $ */
'use strict';

$(document).ready(function(){
    // ---------- Review Category Server-side processing START  ----------
   
    $('#Author-table').DataTable({
        pageLength: 5,
        responsive: true,
        order: [[ 0, "asc" ]],
        columnDefs: [{
            orderable: false,
            targets: [-1, -2]
        },],

        // Ajax for pagination
        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
        },
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'id', name: 'id' },
            { data: 'name', name: 'name' },
            { data: 'email', name: 'email' },
            { data: 'actions', name: 'actions' },

        ],
    });

    $('#book-table').DataTable({
        pageLength: 10,
        responsive: true,
        order: [[ 0, "asc" ]],
        columnDefs: [{
            orderable: false,
            targets: [-1, -2]
        },],

        // Ajax for pagination
        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
        },
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'id', name: 'id' },
            { data: 'title', name: 'title' },
            { data: 'author', name: 'author' },
            { data: 'category', name: 'category' },
            { data: 'actions', name: 'actions' },

        ],
    });


    $('#transaction-table').DataTable({
        pageLength: 10,
        responsive: true,
        order: [[ 0, "asc" ]],
        columnDefs: [{
            orderable: false,
            targets: [-1, -2]
        },],

        // Ajax for pagination
        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
        },
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
        },
        columns: [
            { data: 'id', name: 'id' },
            { data: 'user', name: 'user' },
            { data: 'books', name: 'books' },
            { data: 'issue_date', name: 'issue_date' },
            { data: 'return_date', name: 'return_date' },

        ],
    });



   
    $('#comments-table').DataTable({
        pageLength: 25,
        responsive: true,
        order: [[ 0, "desc" ]],
        columnDefs: [{
            orderable: false,
            targets: [-1, -4, -5]
        },],

        // Ajax for pagination
        "language":
        {
            "processing": "<b><i class='fa fa-refresh fa-spin'></i>&nbsp;Loading....</b>",
        },
        processing: true,
        serverSide: true,
        ajax: {
            url: window.pagination_url,
            type: 'get',
            data: function ( d ) {
                return $.extend( {}, d, {
                    "comment_data": $('#comment_data').val()
                });
            }
        },
        columns: [
            { data: 'id', name: 'id' },
            { data: 'name', name: 'name' },
            { data: 'description', name: 'description', createdCell: function(td, cellData, rowData, row, col) {
                    $(td).addClass('show_description');
                }
            },
            { data: 'in_response_to', name: 'in_response_to' },
            { data: 'create_at', name: 'create_at' },
            { data: 'is_approved', name: 'is_approved', render: is_approved_button},
            { data: 'actions', name: 'actions' },
        ],
        "createdRow": function( row, data, dataIndex){
                if(data['is_approved'] == false){
                    $(row).css('background', '#fcf9e8');
                }
            }
    });

    function is_approved_button(data, type, row, meta){
        if(data === true){
            return '<button onclick="approve_disapprove('+row['id']+', false)" title="Disapprove" class="btn btn-success btn-xs" style="width: 70px;" >Disapprove</button>'
        }else{
            return '<button onclick="approve_disapprove('+row['id']+', true)" title="Approve" class="btn btn-success btn-xs" style="width: 70px;">Approve</button>'
        }
    }

    // ---------- Trusted accessories Server-side processing END  ----------

});

var userroles = {
    // ------------------------------------------------------------------------
    // Users
    // ------------------------------------------------------------------------
    users: {
        index: function () {
            $('#user-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                },
                columns: [
                    { data: 'id', name: 'id' },
                    { data: 'username', name: 'username' },
                    { data: 'name', name: 'name' },
                    { data: 'mobile', name: 'mobile' },
                    { data: 'dob', name: 'dob' },
                    { data: 'is_active', name: 'is_active' },
                    { data: 'created_at', name: 'created_at' },
                    { data: 'actions', name: 'actions' }
                ],
            });

        },

        details: function () {
            $('.groups-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available groups',
                selectedListLabel: 'Chosen groups',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }
    },

    // ------------------------------------------------------------------------
    // Groups
    // ------------------------------------------------------------------------
    groups: {
        index: function () {
            $('#group-table').DataTable({
                pageLength: 25,
                responsive: true,
                order: [[ 0, "desc" ]],
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },]
            });
        },
        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }
    },
};
