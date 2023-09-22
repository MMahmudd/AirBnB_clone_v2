#!/usr/bin/python3
"""This_module defines_a_class to_manage file_storage for_hbnb_clone"""
import json


class FileStorage:
    """This class_manages_storage_of_hbnb_models_in JSON_format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns_a_dictionary _of models_currently_in_storage"""
        if cls is None:
            return self.__objects
        cls_name = cls.__name__
        dct = {}
        for key in self.__objects.keys():
            if key.split('.')[0] == cls_name:
                dct[key] = self.__objects[key]
        return dct

    def new(self, obj):
        """Adds_new_object to_storage_dictionary"""
        self.__objects.update(
            {obj.to_dict()['__class__'] + '.' + obj.id: obj}
            )

    def save(self):
        """Saves_storage dictionary_to_file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads_storage_dictionary_from_file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        ''' deletes_the object_obj_from_the_attribute
            __objects_if it's_inside_it
        '''
        if obj is None:
            return
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        if obj_key in self.__objects.keys():
            del self.__objects[obj_key]

    def close(self):
        """Call_the_re_load_method"""
        self.reload()
