// #include <iostream>

// namespace arhik
// {
//     template <typename Traits>
//     class unique_handle
//     {

//     };

//     struct null_handle_traits
//     {
//         typedef HANDLE pointer;

//         static auto invalid() throw() -> pointer
//         {
//             return nullptr;
//         }

//         static auto close(pointe value) throw() -> void
//         {
//             cout << "Close handle" << endl;
//         }
//     };

//     typedef unique_handle<null_handle_traits> null_handle;

// }