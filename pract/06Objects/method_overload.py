

# # from pythonlangutil.overload import Overload, signature
# from inspect import signature
#
#
#
# class A:
#     @Overload
#     @signature()
#     def stackoverflow(self):
#         print('first method')
#
#     @stackoverflow.overload
#     @signature("int")
#     def stackoverflow(self, i):
#         print 'second method', i