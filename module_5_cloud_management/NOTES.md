# Coursera - Configuration Management and Cloud Management
## Week 1

### Automating with Configuration Management

### What is scale?

`scale` - What we do means we can keep achieving larger impacts with teh same amount of effort.
Example: Automating onboarding to avoid having human interaction, automate application installs to avoid minutes wasted manually clicking, automate ticketing assignment to avoid overload.
A "Scalable" system in a flexible one.

`automation` - essential tools to grow the business with the same amount of people

### What is configuration management?

Manually taking care of actions on a device is called `unmanaged configuration`. This means the OS and applications installed and polices, the whole kit.

Say that the rules and automation that you have rolled out turns out to be unsecure. You can change the rules live and roll out the `patches` to fix the mistakes.

### What is infratstructure as code?

`Infrastructure as code` - (IaC) When all the configuration necessary to deploy and managed a node in the infrastructure is stored in version control

Using `IaC`, this allows your computers or "nodes" to be 
 - Consistent
 - Versioned
 - Reliable
 - Repeatable

### What is Puppet?

`Puppet` - Current configuration management standard used in multiple environments and is cross platform.
The Client is known as the `Puppet Agent`, and the server is known as the `Puppet Master`
The Puppet Agent sends its information to the Puppet Master, the Puppet Master then sends back any changes the Puppet Agent needs to make.
You can use the same Puppet rules across platforms due to the flexibility of the open-source program.

An example of a `Puppet Rule` is here:
```Puppet
class sudo {
	package { 'sudo':
		ensure => present,
	}
}
```

Puppet will check the OS and select the right tool to continue the installations.
On Linux, there are several different package managers `yum` `apt`, and `dnf`.
On MacOS, there is `Apple Provider` for packages that are part of the OS. `MacPorts` for packages that comes from the MacPorts project.
On Windows, there are more steps needed.

### Puppet Resources

```Puppet
class sudo {
	package { 'sudo':
		ensure => present,
	}
}
```
`Resources` - Basic unit for modeling the configuration that we want to manage
Each resources specifies one configuration that we are trying to manage: Package, Service or a File

```Puppet
class sysctl {
	file { '/etc/sysctl.d':
		ensure => directory,
	}
}
```
The above uses a `file` resource to make sure that `'/etc/sys.ctl.d'` was on the system and that it was a directory.
When declaring a resource in Puppet, you delcare the `type`, in this instance it was `file`. The configuration for the resource is written in the curly braces. The `title` comes first, in this case it is `'/etc/stsctl.d'` followed by a colon. After the colon, comes the attributes for the resource.

```Puppet
class timezone {
	file { '/etc/timezone':
		ensure => file,
		content => "UTC\n",
		replace => true,
	}
}
```
The above uses the '/etc/timezone' used by some linux distros.
It checks if the file exists, then ensures the content is 'UTC\n' and if it does exists, it replaces the value instead with the content if it is different.

`Providers` - Puppet will try to decet this automatically and use the appropriate provider to make our rules or 'changes' reali

### Puppet Classes

Puppet Classes can have more than one resource in the config.
```Puppet
class ntp {
	packages { 'ntp':
		ensure => latest,
	}
	file { '/etc/npt.conf':
		source => 'puppet:///modules/ntp/ntp.conf',
		replace => true,
	}
	service { 'ntp':
		enable => true,
		ensure => running,
	}
}
```
`package`
`file`
`service`
when working with resouces, it makes sences to group like minded changes together.

[Puppet Language Syntax](https://puppet.com/docs/puppet/latest/lang_resources.html)

[Puppet with Chocolatey](https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/)


### What are domain-specific languages?

`domain-specific languages` - (DSL) a programming language that is limited in scope
`general-purpose languages` - python, GO - Can be used for numerous projects in different spaces

Puppet's DSL includes `variables`, `conditional statements`, and `functions`.
`Facts` - Variables that represent the characteristics of the system

Example of a puppet process: 
When the Puppet agent runs, it calls a program called factor which analyzes the current system, storing the information it gathers in these facts. Once it's done, it sends the values for these facts to the server, which uses them to calculate the rules that should be applied

```Puppet
if fac
```