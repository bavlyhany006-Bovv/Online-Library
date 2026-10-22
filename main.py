# main.py

from repositories.json_repository import JSONRepository
from services.library_service import LibraryService
from utils.exceptions import LibraryException

def main():
    # 1. تجهيز طبقة التخزين (المخزن)
    repo = JSONRepository()
    
    # 2. تجهيز طبقة الخدمات (المدير)
    service = LibraryService(repo)

    # 3. دورة البرنامج المستمرة (Loop)
    while True:
        print("\n" + "="*40)
        print(" 📚 Online Library Management System ")
        print("="*40)
        print("1. Add a New User")
        print("2. Add a New Book")
        print("3. Search for a Book")
        print("4. Borrow a Book")
        print("5. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-5): ")
        
        try:
            if choice == '1':
                name = input("Enter user name: ")
                email = input("Enter user email: ")
                user = service.add_user(name, email)
                print(f"✅ User '{user.name}' added successfully with ID: {user.id}")
                
            elif choice == '2':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                cat_id = int(input("Enter category ID (e.g., 1): "))
                copies = int(input("Enter available copies: "))
                book = service.add_book(title, author, cat_id, copies)
                print(f"✅ Book '{book.title}' added successfully with ID: {book.id}")
                
            elif choice == '3':
                query = input("Enter title or author to search: ")
                results = service.search_books(query)
                if results:
                    print(f"\n🔍 Found {len(results)} books:")
                    for b in results:
                        print(f"- [ID: {b.id}] {b.title} by {b.author} (Available Copies: {b.available_copies})")
                else:
                    print("❌ No books found matching your query.")
                    
            elif choice == '4':
                user_id = int(input("Enter User ID: "))
                book_id = int(input("Enter Book ID: "))
                if service.borrow_book(user_id, book_id):
                    print("✅ Book borrowed successfully! Copies updated.")
                    
            elif choice == '5':
                print("👋 Exiting the system. Goodbye!")
                break
                
            else:
                print("⚠️ Invalid choice. Please select a number from 1 to 5.")
                
        except ValueError:
            # بيمسك الأخطاء لو اليوزر دخل حروف في مكان المفروض يكون فيه أرقام
            print("❌ Invalid input type! Please enter numbers where expected.")
        except LibraryException as e:
            # هنا بنمسك الاستثناءات المخصصة بتاعتنا (زي الإيميل الغلط أو نسخ الكتب اللي خلصت)
            print(f"⚠️ Business Rule Error: {e}")
        except Exception as e:
            # بيمسك أي خطأ تاني مش متوقع
            print(f"🚨 Unexpected System Error: {e}")

if __name__ == "__main__":
    main()