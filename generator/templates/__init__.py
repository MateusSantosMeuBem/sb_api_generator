MODELS =\
'''package {package_name}.models;

import java.io.Serializable;

import jakarta.persistence.Entity;

@Entity
public class {class_name} implements Serializable <left_brace>

	private static final long serialVersionUID = 1L;

	public {class_name}() <left_brace>
	<right_brace>
<right_brace>

'''

REPOSITORIES =\
'''package {package_name}.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import {package_name}.models.{class_name};

@Repository
public interface {class_name}Repository extends JpaRepository<{class_name}, Long><left_brace>
<right_brace>

'''

SERVICES =\
'''package {package_name}.services;

import java.util.List;

import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import {package_name}.models.{class_name};
import {package_name}.repositories.{class_name}Repository;

@Service
public class {class_name}Service <left_brace>

	@Autowired
	private {class_name}Repository {lower_class_name}Repository;
	
	public {class_name} criar({class_name} {lower_class_name}) <left_brace>
		return {lower_class_name}Repository.save({lower_class_name});
	<right_brace>
    
    public {class_name} buscarPorCodigo(Long codigo) <left_brace>
        {class_name} {lower_class_name} = {lower_class_name}Repository.findById(codigo).orElseThrow();
        return {lower_class_name};
    <right_brace>

	public List<{class_name}> listar() <left_brace>
		return {lower_class_name}Repository.findAll();
	<right_brace>

	public void excluir(Long codigo) <left_brace>
		{lower_class_name}Repository.deleteById(codigo);
	<right_brace>

	public {class_name} atualizar(Long codigo, {class_name} {lower_class_name}) <left_brace>
		{class_name} {lower_class_name}Salva = {lower_class_name}Repository.findById(codigo).orElseThrow();
		BeanUtils.copyProperties({lower_class_name}, {lower_class_name}Salva, "codigo");
		return {lower_class_name}Repository.save({lower_class_name}Salva);
	<right_brace>
<right_brace>

'''

RESOURCES =\
'''package {package_name}.resources;

import java.net.URI;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import jakarta.validation.Valid;
import {package_name}.models.{class_name};
import {package_name}.services.{class_name}Service;


@RestController
@RequestMapping("/{lower_class_name}s")
public class {class_name}Resource <left_brace>
	
	@Autowired
	private {class_name}Service {lower_class_name}Service;
	
	@PostMapping
	public ResponseEntity<{class_name}> criar(@Valid @RequestBody {class_name} {lower_class_name})<left_brace>
		{class_name} {lower_class_name}Salva = {lower_class_name}Service.criar({lower_class_name});		
		URI uri = ServletUriComponentsBuilder.fromCurrentRequest().path("/<left_brace>codigo<right_brace>").buildAndExpand({lower_class_name}Salva.getCodigo()).toUri();
		return ResponseEntity.created(uri).body({lower_class_name}Salva);
	<right_brace>
	
	@GetMapping
	public ResponseEntity<List<{class_name}>> listar()<left_brace>
		List<{class_name}> {lower_class_name}s = {lower_class_name}Service.listar();
		return ResponseEntity.ok().body({lower_class_name}s);
	<right_brace>
	
	@GetMapping(value = "/<left_brace>codigo<right_brace>")
	public ResponseEntity<{class_name}> buscarPorCodigo(@PathVariable Long codigo)<left_brace>
		{class_name} {lower_class_name} = {lower_class_name}Service.buscarPorCodigo(codigo);
		return ResponseEntity.ok().body({lower_class_name});
	<right_brace>
	
	@DeleteMapping(value="/<left_brace>codigo<right_brace>")
	public ResponseEntity<Void> excluir(@PathVariable Long codigo)<left_brace>
		{lower_class_name}Service.excluir(codigo);
		return ResponseEntity.noContent().build();
	<right_brace>
	
	@PutMapping(value="/<left_brace>codigo<right_brace>")
	public ResponseEntity<{class_name}> atualizar(@PathVariable Long codigo,@Valid @RequestBody {class_name} {lower_class_name})<left_brace>
		{class_name} {lower_class_name}Salva = {lower_class_name}Service.atualizar(codigo, {lower_class_name});
		return ResponseEntity.ok().body({lower_class_name}Salva);
	<right_brace>
<right_brace>

'''

struct = {
	'models': MODELS,
	'repositories': REPOSITORIES,
	'services': SERVICES,
	'resources': RESOURCES,
}