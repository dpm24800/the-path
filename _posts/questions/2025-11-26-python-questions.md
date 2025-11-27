

**Which database does Django use?**

Django officially supports several relational databases, and the choice depends on the project's requirements.

By default, Django uses SQLite. This is a lightweight, file-based database that is included with Python and requires no additional installation, making it ideal for development, testing, and small projects.

For production environments and larger applications, Django offers robust support for other databases, including:

- **PostgreSQL:** 
  Often considered the best choice for Django due to its advanced features, reliability, and strong community support.

- **MySQL:** 
  A popular and widely used database, suitable for various web applications.

- **MariaDB:** 
  A community-developed fork of MySQL, offering similar features and performance.

- **Oracle:** 
  Used in enterprise-level applications that already utilize Oracle databases.

Django's Object-Relational Mapper (ORM) provides an abstraction layer that allows developers to interact with the database using Python code, largely shielding them from the underlying database specifics. This enables easy switching between supported database engines with minimal code changes.