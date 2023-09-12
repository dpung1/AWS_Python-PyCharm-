from userManagement.util.ResponseUtil import ResponseEntity

class UserController:

    @staticmethod
    def registerUser(user = None):
        from userManagement.repository.UserRepository import UserRepository
        responseBody = bool(UserRepository.saveUser(user))

        return ResponseEntity(body=responseBody)
