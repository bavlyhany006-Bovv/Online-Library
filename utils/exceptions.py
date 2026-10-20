class LibraryException(Exception):
    """الاستثناء الرئيسي للنظام - ترث منه كافة الاستثناءات الأخرى."""
    pass

class ValidationError(LibraryException):
    """يرمى عند وجود خطأ في صحة البيانات المدخلة (مثل إيميل خاطئ أو تقييم غير مسموح)."""
    pass

class NotFoundError(LibraryException):
    """يرمى عند البحث عن كيان غير موجود (مستخدم، كتاب، قسم)."""
    pass

class DuplicateError(LibraryException):
    """يرمى عند محاولة إضافة عنصر موجود مسبقاً (مثل إيميل مكرر أو تقييم مكرر)."""
    pass